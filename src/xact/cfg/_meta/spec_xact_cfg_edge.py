# -*- coding: utf-8 -*-
"""
Functional specification for the xact.cfg.edge module.

"""


# =============================================================================
class SpecifyDenormalize:
    """
    Spec for the edge.denormalize function.

    """

    # -------------------------------------------------------------------------
    def it_adds_fields(self, valid_normalized_config):
        """
        Check edge.denormalize adds fields to the config structure.

        """
        import xact.cfg.edge  # pylint: disable=C0415

        cfg_denorm = xact.cfg.edge.denormalize(valid_normalized_config)

        for cfg_edge in cfg_denorm['edge']:
            for key in ('id_edge',      'relpath_src', 'relpath_dst',
                        'id_node_src',  'id_node_dst', 'list_id_process',
                        'list_id_host', 'ipc_type',    'id_host_owner',
                        'id_host_src',  'id_host_dst', 'idx_edge'):
                assert key in cfg_edge

        for cfg_host in cfg_denorm['host'].values():
            assert 'is_inter_host_edge_owner' in cfg_host
